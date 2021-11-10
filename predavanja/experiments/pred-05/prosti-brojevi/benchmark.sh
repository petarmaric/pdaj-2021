#! /bin/bash -eu

TEST_ITERATIONS=(
  10
  100
  1000

  2000
  3000

  # 4000

  # 5000
)

PROGRAMS=*.py
PROGRAMS_BLACKLIST=(
  'map_v2.py'
  'map_v3.py'

  'imap_v1.py'
  'imap_v2.py'
  'imap_v3.py'

  'imap_un_v1.py'
  'imap_un_v2.py'
  'imap_un_v3.py'
)


for max_num in ${TEST_ITERATIONS[*]}; do
  echo "max_num = $max_num"

  echo -e "program \t time   \t CPU \t RAM (KB)"
  for program in $PROGRAMS; do
    if [[ " ${PROGRAMS_BLACKLIST[@]} " =~ " $program " ]]; then
        # echo -e "$program \t TOO SLOW!"
        true # no-op
    else
      /usr/bin/time -f "$program \t %E \t %P \t %M" python3 $program --max-num=$max_num
    fi
  done

  echo ""
done
