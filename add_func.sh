#!/bin/sh

#定义函数main
 main () {
    need_cmd curl
    echo "bash" # arguments are accessible through $1, $2,...
}
#定义函数need_cmd
need_cmd() {
    echo "need"
    if ! check_cmd "$1"; then
        err "need '$1' (command not found)"
    fi
}
check_cmd() {

   command -v "$1" > /dev/null 2>&1
  #command指执行时不查shell中的函数，查bash命令表中的命令， 比如 command curl -v ,指查询curl命令，不是curl函数
   # command -v "$1" 
   echo "check"
  
}

say() {
    printf 'pulsar-install: %s\n' "$1"
}

err() {
    say "$1" #>&2
   # exit 1
}

#执行函数main
main "$@" || exit 1