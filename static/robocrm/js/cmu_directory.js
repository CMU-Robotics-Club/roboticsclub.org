$(document).ready(function(){
  $("#id_username").focusout(function(){
    var andrewID = $(this).val()

    $.getJSON("/crm/directory_info/" + andrewID, function(info) {
        var first_name = "";
        var last_name = "";
        var email = "";
        var major = "";
        var grad_year = "";
        var class_level = null;

        first_name = info["first_name"];
        last_name = info["last_name"];
        email = info["preferred_email"];
        major = info["department"];

        var role = info["affiliation"];
        var student_class = info["student_class"];
        var student_level = info["student_level"];

        if (role == "Student") {
          var year_offset = null;

          switch(info["student_class"]) {
            case "Senior": {
              year_offset = 0;
              break;
            }
            case "Junior": {
              year_offset = 1;
              break;
            }
            case "Sophmore": {
              year_offset = 2;
              break;
            }
            case "Freshman": {
              year_offset = 3;
              break;
            }
          }

          var date = new Date();
          var current_year = date.getFullYear();
          // Spring if current month is less than June else new year
          var is_spring = (date.getMonth() < 5);
          if(!is_spring) {
            //If in the Fall graduation is following year
            year_offset += 1;
          }

          if (year_offset) {
            grad_year = current_year + year_offset;
          }
        }

        var class_level = null;

        if(student_level == "Undergrad") {
          class_level = 0;
        }
        else if(student_level == "Graduate") {
          class_level = 1;
        }
        else if(role == "Faculty") {
          class_level = 2;
        }

      $("#id_first_name").val(first_name);
      $("#id_last_name").val(last_name);
      $("#id_email").val(email);
      $("#id_robouser-0-major").val(major);
      $("#id_robouser-0-grad_year").val(grad_year);
      $("#id_robouser-0-class_level>option:eq(" + class_level + ")").prop('selected', true);
    });
  });
});
