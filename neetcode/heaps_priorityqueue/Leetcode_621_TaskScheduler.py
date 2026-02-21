class LabelInfo:
    def __init__(self, label:str, jobsLeft:int, lastCpuTimeOfRunning:int):
        self.label = label
        self.jobsLeft = jobsLeft
        self.lastCpuTimeOfRunning = lastCpuTimeOfRunning
    
    def __repr__(self):
        return f"jobsLeft={self.jobsLeft}, lastCpuTimeOfRunning={self.lastCpuTimeOfRunning}"

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        return self.leastIntervalMyBruteForce( tasks, n )
    
    def leastIntervalMyBruteForce(self, tasks: list[str], n: int) -> int:

        idleGap = n

        lableAndItsInfo:dict[str:LabelInfo] = {}
        #Populating the dictionary
        for task in tasks:
            labelInfoObj = lableAndItsInfo.get( task, LabelInfo(task, 0, -(1<<31)) )
            labelInfoObj.jobsLeft += 1
            lableAndItsInfo[task] = labelInfoObj
            
        print( lableAndItsInfo )
        
        cpuTime = 0
        while len(lableAndItsInfo) > 0:
            bestLabelInfoToPickNow =  LabelInfo("dummy_label", -(1<<31), -1  )#Will initialize with a dummy label so that we can replace it with the actual label
            for labelItr in lableAndItsInfo.keys():
                # print(f"Hi1:{labelItr}")
                # print(f"Hi1:{lableAndItsInfo[labelItr].lastCpuTimeOfRunning}")
                # print(f"Hi1:{lableAndItsInfo[labelItr].jobsLeft > bestLabelInfoToPickNow.jobsLeft}")

                if ( lableAndItsInfo[labelItr].lastCpuTimeOfRunning + idleGap + 1 <= cpuTime ) and (lableAndItsInfo[labelItr].jobsLeft > bestLabelInfoToPickNow.jobsLeft):
                    bestLabelInfoToPickNow = lableAndItsInfo[labelItr]

            if bestLabelInfoToPickNow.label == "dummy_label":
                # No jobs are ready to be running, will have to go idle
                # print(f"Going idle on cpuTime={cpuTime} ")
                ""
            else:
                # print(f"At cpuTime={cpuTime}, executing the label={bestLabelInfoToPickNow.label}")

                lableAndItsInfo[bestLabelInfoToPickNow.label].jobsLeft -= 1
                lableAndItsInfo[bestLabelInfoToPickNow.label].lastCpuTimeOfRunning = cpuTime
                
                if lableAndItsInfo[bestLabelInfoToPickNow.label].jobsLeft == 0:
                    lableAndItsInfo.pop(  bestLabelInfoToPickNow.label  )


            cpuTime += 1

        # In the question the cpu time spent is one based indexing, as we have already added 1 in the end of the while loop, we can return the variable value
        return cpuTime



tasksToRun =  ["A","A","A","B","B","B"]
idleGapToKeep = 3
print( Solution().leastInterval(tasksToRun, idleGapToKeep) )