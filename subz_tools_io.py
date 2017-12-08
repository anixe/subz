import os
import subprocess
from subprocess import PIPE

def is_dir(path):
    return os.path.isdir(path)

def is_file(path):
    return os.path.isfile(path)

# from: https://stackoverflow.com/a/377028/540761
def is_exe(path):
    return is_file(path) and os.access(path, os.X_OK)

# from: https://stackoverflow.com/a/377028/540761
def which(program):
  path, fname = os.path.split(program)
  if path:
      if is_exe(program):
          return program
  else:
      for path in os.environ["PATH"].split(os.pathsep):
          path = path.strip('"')
          exe_file = os.path.join(path, program)
          if is_exe(exe_file):
              return exe_file

  return None

def run(cmd, args, stdin=None):
  cmd_and_args = '"{}" {}'.format(cmd, args)
  child     = subprocess.Popen(cmd_and_args, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
  raw_stdin = stdin.encode('utf-8') if stdin != None else None
  raw_stdout, raw_stderr = child.communicate(input=raw_stdin)
  stdout    = raw_stdout.decode('utf-8').strip() if raw_stdout else ""
  stderr    = raw_stderr.decode('utf-8').strip() if raw_stderr else ""
  errcode   = child.returncode

  return (stdout, stderr, errcode, cmd_and_args)