#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>


void rearrange(char *str)
{
  int length = strlen(str);
  srand(time(NULL));


  for (int i = length - 1; i > 0; i--)  {
        int j = rand() % (i + 1);
        char swap = str[i];
        str[i] = str[j];
        str[j] = swap;
  }

}

int main()
{
  const int MAX = 50;

  char target[MAX];
  printf("Enter a word to be diffused: ");
  fgets(target, MAX, stdin);

  target[strcspn(target, "\n")] = NULL;

  rearrange(target);
  printf("Diffused word: %s\n", target);

  return 0;
}
