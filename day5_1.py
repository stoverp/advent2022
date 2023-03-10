import re
from argparse import ArgumentParser
from collections import defaultdict


def print_stacks(stacks):
  for i in range(len(stacks)):
    print(f"{i + 1}: {stacks[i + 1]}")


def read_stacks(f):
  stacks = defaultdict(list)
  while "[" in (line := f.readline()):
    print(line.rstrip())
    pos = 0
    stack = 1
    while pos < len(line.rstrip()):
      if "[" in (container_str := line[pos:pos+3]):
        stacks[stack].append(container_str[1])
      pos += 4
      stack += 1
  print("initial stacks:")
  print_stacks(stacks)
  return stacks


def execute_move(line, stacks):
  if match := re.match("move (?P<count>\d+) from (?P<name>\d+) to (?P<dest_pos>\d+)", line):
    print(line.rstrip())
    count = int(match.group("count"))
    source_stack = int(match.group("name"))
    dest_stack = int(match.group("dest_pos"))
    for i in range(count):
      container = stacks[source_stack].pop(0)
      stacks[dest_stack].insert(0, container)
      # print(f"moved {container} from stack {source_stack} to {dest_stack}. stacks: {stacks}")
  else:
    raise Exception(f"invalid input line: {line}")


def main(file):
  with open(file, "r") as f:
    stacks = read_stacks(f)
    for line in f:
      if "move" not in line:
        continue
      execute_move(line, stacks)
  print(f"top of stacks: {''.join([stacks[i + 1][0] for i in range(len(stacks))])}")


if __name__ == "__main__":
  parser = ArgumentParser()
  parser.add_argument("file")
  args = parser.parse_args()
  main(args.file)
