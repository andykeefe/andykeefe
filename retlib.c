// ------------------------------------------------------------------------------- //
// The fread function is vulnerable to a buffer overflow because it relies on other
// function to check for errors. By not including those functions here, the program
// is made vulnerable.
// ------------------------------------------------------------------------------- //


#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int bof(FILE *badfile)
{

   char buffer[12];
                                              // ----------------------------------//
   fread(buffer, sizeof(char), 40, badfile);  // Using fread without error handling
                                              // functions feof and ferror
                                              // ----------------------------------//
   return 1;

}

// ------------------------------------------------------------------------------- //
// Running the program loads libc into memory. By setting a breakpoint at the main
// function and running the program in the debugger, you can load libc and find 
// its address.
// ------------------------------------------------------------------------------- //


int main(int argc, char **argv)
{

   FILE *badfile;

   badfile = fopen("badfile", "r");

   bof(badfile);

   printf("Returned properly\n");

   fclose(badfile);
   return 1;

}

