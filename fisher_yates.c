/* This is an implementation of the Fisher-Yates shuffle algorithm in C. It is intended to 
  randomly shuffle a finite sequence like a message that is input by the user, in this case,
  me. This shuffling algorithm can be considered a "transposition cipher" and captures the 
  cryptographic property of diffusion, though not substitution. 
  
  In Applied Cryptography by Bruce Schneier, he notes that "the simplest way to cause diffusion 
  is through transposition" (p. 237). For that reason, this code can be useful to demonstrate 
  one of two basic techniques in obscuring statistical redundancies. */
 

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>


void rearrange(char *str)
{
  int length = strlen(str);
  
  srand(time(NULL));  /* This line is key to the randomness of the algorithm
                      because it generates a random seed based on the current time. 
                      
                      The same word will be "encrypted" in different ways each time
                      it is used as input. This is because of the randomized seed. */


                      /* int i is initialized to the last character in the input in the first line
                        and for loop continues so long as there is still input. int j is a random number
                        between zero and the length of the input. */
 
  for (int i = length - 1; i > 0; i--)  {
        int j = rand() % (i + 1);     
        char swap = str[i];
        str[i] = str[j];
        str[j] = swap;
  }  
                            /* A char variable, swap, is created using the index at the last value in the input array. 
                              We then substitute the char at str[i], the last char, with the randomly derived char at 
                              str[j]. The value where str[j] was is then made the swap value. This repeats until i = 0. */
  
  
}

int main()
{
  const int MAX = 50;

  char target[MAX];
  printf("Enter a word to be diffused: ");
  fgets(target, MAX, stdin);

  target[strcspn(target, "\n")] = NULL;  /* This is an elegant way to drop the newline character 
                                          before beginning the Fisher-Yates shuffle. 

                                          strcspn(string, char) reads the string up until the defined character
                                          char, then returns the length of the string up to that point. We then use
                                          that number to index the newline character and set it to NULL. That way, it
                                          won't sour the output.  */

  rearrange(target);
  printf("Diffused word: %s\n", target);

  return 0;
}
