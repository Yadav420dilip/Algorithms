"""In job sequencing problem, the objective is to find a sequence of jobs, which is completed within their deadlines
and gives maximum profit using greedy method. """


def job_sequencing(tasks, time):
    """This method arrange the job for the maximum profit in the given deadline ."""
    tasks.sort(key=lambda x: x[1], reverse=True)    # Sort the job in the decreasing order
    job = [0] * time    # list for store the job
    time_space = [False] * time     # to track the free time space
    profit = 0

    # iterating the task
    for task in tasks:

        #   this loop for finding the available time slot for particular time slot
        for i in range(task[2]-1, -1, -1):
            if time_space[i] is False:      # Check the free time slot
                job[i] = task[0]
                profit += task[1]
                time_space[i] = True
                break

    print("Job Sequence ", job)
    print(profit)


"""Data format
    [[job name, Profit, deadline],
    []]"""
tasks = [["job1", 20, 2],
         ["job2", 15, 2],
         ["job3", 10, 1],
         ["job5", 1, 3],
         ["job4", 5, 3]]

job_sequencing(tasks, 3)
