// -------------------------------------------- //
// This program finds the environment variable
// created, MYSHELL, which I set to /bin/zsh
// -------------------------------------------- //


#include <stdio.h>
#include <stdlib.h>


int main()
{						// ------------------------------------ //
   char *shell = (char *)getenv("MYSHELL");	// getenv returns environment string
						// of MYSHELL, the custom env variable
						// ------------------------------------ //
   if(shell)  {
								// ---------------------------- //
	printf("	Value:  %s\n", shell);			// if statement prints the 
	printf("	Address: %x\n", (unsigned int)shell);	// name and address of MYSHELL
   								// ---------------------------- //
   } 

   return 1;

}
