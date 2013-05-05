#include "log.h"
#include <stdio.h>
#include <stdarg.h>
#include <time.h>
#include <errno.h>
#include <sys/time.h>

void log_time() {
  char buf[100];
  time_t t;
  time(&t);
  strftime(buf, sizeof(buf), "%b %e %T %Y", localtime(&t));
  printf("[%s] ", buf);
}

void log_print(const char *fmt, ...) {
  va_list args;
  va_start(args, fmt);
  log_time();
  vprintf(fmt, args);
  printf("\n");
  va_end(args);
}

void log_perror(const char *s) {
  log_time();
  perror(s);
}
