#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 *infinite_while - entry point
 *
 *Return: 0 on success
 */
int infinite_while(void)
{
while (1)
{
sleep(1);
}
return (0);
}

/**
 *main - entry point
 *
 *Return: 0 on success
 */
int main(void)
{
pid_t pid;
int x;

for (x = 0; x < 5; x++)
{
pid = fork();
if (pid == 0)
exit(0);
printf("Zombie process created, PID: %d\n", pid);
}
infinite_while();
return (0);
}
