// A program with a buffer overflow vulnerability //
// I'm going to meticulously comment throughout the code to better understand
// the specifics of what's going on at each part of the program. //
// If that makes the code challenging to read, sorry! //
// But it helps me learn, and that's what I'm focused on. //



#include <stdlib.h>
#include <stdio.h>
#include <string.h>


int bof(char *str)
{
    char buffer[24];

    strcpy(buffer, str);  // The root of the buffer overflow issue //
			  // strcpy() doesn't check for boundaries //	

    return 1;
}


int main(int argc, char **argv)
{
    char str[517];
    FILE *badfile;

    badfile = fopen("badfile", "r");  // Input for program is from badfile //
    fread(str, sizeof(char), 517, badfile);

    		// Input read from badfile is passed to buffer in function bof() //

    bof(str);  // bof() buffer has only 24 bytes, but the input can have 517 bytes //
  

    printf("Returned properly.\n");
    return 1;
}
