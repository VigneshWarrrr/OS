#include<stdio.h> 
#include<stdlib.h> 
#include<sys/wait.h> 
#include<unistd.h> 

void main()
{
    int pid;
    pid=fork();
    if(pid<0)
    {
        printf("Fork Fail");
        exit(1);
    }else if(pid==0){
        printf("Now in child Process and its output is:\n");
        execlp("ls","ls",NULL);
        exit(0);
    }else{
        printf("Child Process Created Successfully.");
        printf("\n\t Process id: %d\n",getpid());
        wait(NULL);
        printf("Return back to parent process.Now ready to exit");
        exit(0);
    }
}
