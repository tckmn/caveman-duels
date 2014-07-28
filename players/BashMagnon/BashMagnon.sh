#!/bin/bash

function min () {
 [[ $1 -gt $2 ]] && echo $2 || echo $1
}

function max () {
[[ ${1%% *} -gt ${2%% *} ]] && echo $1 || echo $2
}

declare -A brain
declare -i C S P B me he
he=0
me=0
C=0
S=0; B=0; P=0

left=${1%%,*}
right=${1##*,}
while  : 
do

    [[ "${right:$C:1}" ]] && brain[$he$me]=${right:$C:1}
    case "${left:$C:1}${right:$C:1}" in
    BB) true;;
    BP) ((he--));;
    BS) ((he++));;
    PP) ((he--)); ((me--));;
    PB) ((me--));;
    PS|SP) exit;;
    SB) ((me++));;
    SS) ((me++)); ((he++));;
    "") break;;
    esac
    me=$(max 0 $me)
    me=$(min 9 $me)
    he=$(max 0 $he)
    he=$(min 9 $he)
    ((C++))
done

[[ $me$he =  *[5-9] ]] && ((P+=2))
[[ $me$he =  [5-9]* ]] && ((P+=2))
[[ $me$he =  [1-9]0 ]] && ((P+=2))
[[ $me$he =  00 ]] && ((S+=2))
[[ $me$he =  [1-4]4 ]] && ((P+=2))
[[ $me$he =  0[1-4] ]] && ((S+=1))
[[ $me$he =  0* ]] && ((B+=1))

case "${brain["$he$me"]}" in 
S) ((P+=2));;
B) ((S+=2));;
P) ((B+=2));;
*) ((B++));;
esac

set $(max "$B B" "$(max "$P P" "$S S")" )
echo $2