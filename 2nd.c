#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
int pid;


pid = fork();

if (pid < 0) {
    perror("Fork Failed");
    exit(1);
}
else if (pid == 0) {
    printf("Child process PID: %d, PPID: %d\n", getpid(), getppid());
    exit(0);
}
else {
    wait(NULL);
    printf("Parent Process PID: %d, PPID: %d\n", getpid(), getppid());
}

return 0;


}
