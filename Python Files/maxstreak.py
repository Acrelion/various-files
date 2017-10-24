# finds the longest streak of numbers who are the same in the given array.
# works also with strings

#arr = [1,1,2,2,2,5,7,1,1]
arr = ["B", "a", "a", "a", "v", "v", "e", "n"]

start = 0
end = 0
currentstart = 0
currentend = 0
digit = arr[0]
streak = 1
maxstreak = 1
mostcommon = arr[0]


for item in range(1, len(arr) - 1):
    if digit == arr[item]:
        streak += 1
        currentend = item
    else:
        digit = arr[item]
        streak = 1
        currentstart = item


    if streak > maxstreak:
        mostcommon = digit
        maxstreak = streak
        start = currentstart
        end = currentend


print "Start", start
print "End", end
print "Most common digit", mostcommon
print "Streak", maxstreak
        
        
        
