#include <stdio.h>

struct Process
{
    int pid;
    int burst;
    int priority;
    int waiting;
    int turnaround;
};

/* Function to display results */
void display(struct Process p[], int n)
{
    int i;
    float avg_wait = 0, avg_turnaround = 0;

    printf("\nPID\tBurst\tWait\tTurnaround\n");

    for (i = 0; i < n; i++)
    {
        printf("%d\t%d\t%d\t%d\n",
               p[i].pid,
               p[i].burst,
               p[i].waiting,
               p[i].turnaround);

        avg_wait += p[i].waiting;
        avg_turnaround += p[i].turnaround;
    }

    printf("\nAverage Waiting Time = %.2f\n", avg_wait / n);
    printf("Average Turnaround Time = %.2f\n",
           avg_turnaround / n);
}


/* ---------------- FCFS ---------------- */

void FCFS(struct Process p[], int n)
{
    int i;

    p[0].waiting = 0;

    for (i = 1; i < n; i++)
    {
        p[i].waiting =
            p[i - 1].waiting + p[i - 1].burst;
    }

    for (i = 0; i < n; i++)
    {
        p[i].turnaround =
            p[i].waiting + p[i].burst;
    }

    printf("\n===== FCFS Scheduling =====\n");

    display(p, n);
}


/* ---------------- SJF ---------------- */

void SJF(struct Process p[], int n)
{
    int i, j;
    struct Process temp;

    /* Sort according to burst time */
    for (i = 0; i < n - 1; i++)
    {
        for (j = i + 1; j < n; j++)
        {
            if (p[i].burst > p[j].burst)
            {
                temp = p[i];
                p[i] = p[j];
                p[j] = temp;
            }
        }
    }

    p[0].waiting = 0;

    for (i = 1; i < n; i++)
    {
        p[i].waiting =
            p[i - 1].waiting + p[i - 1].burst;
    }

    for (i = 0; i < n; i++)
    {
        p[i].turnaround =
            p[i].waiting + p[i].burst;
    }

    printf("\n===== SJF Scheduling =====\n");

    display(p, n);
}


/* ---------------- Priority ---------------- */

void Priority(struct Process p[], int n)
{
    int i, j;
    struct Process temp;

    /*
       Lower priority number = Higher priority
       Example:
       Priority 1 > Priority 2 > Priority 3
    */

    for (i = 0; i < n - 1; i++)
    {
        for (j = i + 1; j < n; j++)
        {
            if (p[i].priority > p[j].priority)
            {
                temp = p[i];
                p[i] = p[j];
                p[j] = temp;
            }
        }
    }

    p[0].waiting = 0;

    for (i = 1; i < n; i++)
    {
        p[i].waiting =
            p[i - 1].waiting + p[i - 1].burst;
    }

    for (i = 0; i < n; i++)
    {
        p[i].turnaround =
            p[i].waiting + p[i].burst;
    }

    printf("\n===== Priority Scheduling =====\n");

    display(p, n);
}


/* ---------------- Round Robin ---------------- */

void RoundRobin(struct Process p[], int n, int quantum)
{
    int remaining[n];
    int i;
    int time = 0;
    int completed = 0;

    for (i = 0; i < n; i++)
    {
        remaining[i] = p[i].burst;
        p[i].waiting = 0;
        p[i].turnaround = 0;
    }

    while (completed < n)
    {
        for (i = 0; i < n; i++)
        {
            if (remaining[i] > 0)
            {
                if (remaining[i] > quantum)
                {
                    time += quantum;
                    remaining[i] -= quantum;
                }
                else
                {
                    time += remaining[i];

                    p[i].turnaround = time;
                    p[i].waiting =
                        p[i].turnaround - p[i].burst;

                    remaining[i] = 0;
                    completed++;
                }
            }
        }
    }

    printf("\n===== Round Robin Scheduling =====\n");
    printf("Time Quantum = %d\n", quantum);

    display(p, n);
}


/* ---------------- Main Function ---------------- */

int main()
{
    int n, i, choice;
    int quantum;

    printf("Enter number of processes: ");
    scanf("%d", &n);

    struct Process p[n];

    for (i = 0; i < n; i++)
    {
        p[i].pid = i + 1;

        printf("Enter burst time for P%d: ", i + 1);
        scanf("%d", &p[i].burst);

        printf("Enter priority for P%d: ", i + 1);
        scanf("%d", &p[i].priority);
    }

    printf("\n1. FCFS  2. SJF  3. Priority  4. Round Robin\n");

    printf("Enter choice: ");
    scanf("%d", &choice);

    switch (choice)
    {
        case 1:
            FCFS(p, n);
            break;

        case 2:
            SJF(p, n);
            break;

        case 3:
            Priority(p, n);
            break;

        case 4:
            printf("Enter time quantum: ");
            scanf("%d", &quantum);

            RoundRobin(p, n, quantum);
            break;

        default:
            printf("Invalid choice!\n");
    }

    return 0;
}
