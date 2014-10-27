from rest_framework import viewsets
from robocrm.models import RoboUser
from projects.models import Project
from officers.models import Officer
from webcams.models import Webcam
from social_media.models import SocialMedia
from sponsors.models import Sponsor
from rest_framework.response import Response
from channels.models import Channel
from rest_framework.parsers import JSONParser
#from rest_framework.decorators import detail_route, list_route
from rest_framework.decorators import *
from .serializers import *
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.exceptions import APIException, ParseError, NotAuthenticated, AuthenticationFailed, PermissionDenied
from .errno import *
from .google_api import get_calendar_events
import dateutil.parser
from django.conf import settings
from django.utils import timezone
from .filters import RoboUserFilter, ChannelFilter
from rest_framework.viewsets import GenericViewSet


# TODO: figure out why import detail_route and list_route does not work
def detail_route(methods=['get'], **kwargs):
  def decorator(func):
    func.bind_to_methods = methods
    func.list = False
    func.detail = True
    func.kwargs = kwargs
    return func
  return decorator

def list_route(methods=['get'], **kwargs):
  def decorator(func):
    func.bind_to_methods = methods
    func.detail = False
    func.list = True
    func.kwargs = kwargs
    return func
  return decorator


class LoginViewSet(viewsets.ViewSet):
  """
  Return True if the fields 'username' and 'password'
  in a POST request are valid user credentials.
  """

  # So details can easily be gotten through
  # browsing the API
  def list(self, request):
    error = ParseError(detail="Username and Password must be provided")
    error.errno = USERNAME_OR_PASSWORD_NONE
    raise error

  # Actual action
  def create(self, request):
    data = JSONParser().parse(request)
    username = data.get('username', None)
    password = data.get('password', None)

    if username is None or password is None:
      error = ParseError(detail="Username and Password must be provided")
      error.errno = USERNAME_OR_PASSWORD_NONE
      raise error

    user = authenticate(username=username, password=password)

    valid = user is not None
    return Response(valid)
    

class WebcamViewSet(viewsets.ReadOnlyModelViewSet):
  """
  The Club's Webcams.
  """

  model = Webcam
  serializer_class = WebcamSerializer
  filter_fields = ('id', 'name', )

class DateTimeViewSet(viewsets.ViewSet):
  """
  The current datetime.  Exists so that projects
  without a realtime clock can easily get the datetime.
  """

  def list(self, request):
    return Response(timezone.now())

class RoboUserViewSet(viewsets.ReadOnlyModelViewSet):
  """
  The members of the Robotics Club.
  """

  model = RoboUser
  serializer_class = RoboUserSerializer
  filter_class = RoboUserFilter

  @detail_route(methods=['POST'])
  def rfid(self, request, pk):
    user = request._user

    if type(user).__name__ != 'Project':
      error = PermissionDenied(detail="Not authenticated as a project")
      error.errno = NOT_AUTHENTICATED_AS_PROJECT
      raise error
    elif user.id not in settings.RFID_POST_PROJECT_IDS:
      error = PermissionDenied(detail="This project is not authenticated to perform this operation")
      error.errno = INSUFFICIENT_PROJECT_PERMISSIONS
      raise error
    else:
      u = RoboUser.objects.filter(pk=pk)[0]

      rfid = request.DATA

      if not rfid:
        error = ParseError(detail="Empty RFID #")
        error.errno = EMPTY_POST
        raise error
      else:
        u.rfid = rfid
        u.save()

        return Response(True)

class OfficerViewSet(viewsets.ReadOnlyModelViewSet):
  """
  The officers of the Robotics Club.
  """

  model = Officer
  serializer_class = OfficerSerializer
  filter_fields = ('id', 'position', 'user', 'order', )

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
  """
  Club Projects
  """

  model = Project
  serializer_class = ProjectSerializer
  filter_fields = ('id', 'name', 'display', 'leaders', )

  @detail_route(methods=['get', 'post'])
  def datastore(self, request, pk):
    # TODO: implement
    pk = int(pk)

    return Response()  

class ChannelViewSet(viewsets.ModelViewSet):

  model = Channel
  serializer_class = ChannelSerializer
  filter_class = ChannelFilter

class SponsorViewSet(viewsets.ReadOnlyModelViewSet):
  model = Sponsor
  serializer_class = SponsorSerializer
  filter_fields = ('id', 'name', 'active', )

class SocialMediaViewSet(viewsets.ReadOnlyModelViewSet):
  model = SocialMedia
  serializer_class = SocialMediaSerializer
  filter_fields = ('id', 'name', )

class CalendarViewSet(viewsets.ViewSet):
  """
  Returns a list of events currently occuring on the club's calendar.
  Each event has the field 'name', 'location', 'start_time', and 'end_time'.
  The 'current time' can be changed by setting the URL parameter 'dt' to a specified datetime.
  """

  def list(self, request):
    """
    List the calendar events.
    """

    dt = self.request.QUERY_PARAMS.get('dt', None)

    if not dt:
      # If no datetime specified use now
      dt = timezone.now()
    else:
        dt = dateutil.parser.parse(dt)

    events = get_calendar_events(dt)
    return Response(events)

class MagneticViewSet(viewsets.ViewSet):
  """
  Returns the RoboUser ID associated with the specified CMU Card ID.
  """

  def create(self, request):
    """
    Returns the RoboUser ID associated with the Card ID sent in the POST body.
    """

    card_id = request.DATA

    try:
      robouser = RoboUser.objects.get(magnetic=card_id)
      return Response(robouser.id)
    except RoboUser.DoesNotExist:
      error = APIException(detail="Magnetic ID has no such member")
      error.errno = MAGNETIC_NO_MEMBER
      raise error

class RFIDViewSet(viewsets.ViewSet):
  """
  Returns the RoboUser ID associated with the specified CMU RFID tag.
  """

  def create(self, request):
    rfid = request.DATA

    try:
      robouser = RoboUser.objects.get(rfid=rfid)
      return Response(robouser.id)
    except RoboUser.DoesNotExist:
      error = APIException(detail="RFID has no such member")
      error.errno = RFID_NO_MEMBER
      raise error
