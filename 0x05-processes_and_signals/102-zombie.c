#inlcude <stdio.h>
#inlcude <stdlib.h>
#include <unistd.h>
/**
 * main - 
 * 
 * Return - 
 */
int main(void):
{
pid_t pid;
int x;

    for(x = 0; x < 5; x++)
    {
        pid = fork();
        if (pid == 0)
            exit(0);
            printf("Zombie process created, PID: %d", pid)
    }
    infinite_while();
    return (0);
}


int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}