## 2073. Time Needed to Buy Tickets
[2073 LeetCode Link](https://leetcode.com/problems/time-needed-to-buy-tickets)

This solution efficiently simulates the ticket buying process. The time complexity is O(n*m) where n is the number of people in the queue and m is the maximum number of tickets a person wants to buy. Though not the most efficient in terms of time complexity, given the constraints, this solution works well for the input size specified.

To solve this problem, we'll simulate the process of buying tickets. We keep track of the total time taken and reduce the number of tickets for each person by one in each pass until the person at position k has bought all their tickets. Here's the strategy:

- Initialize a time counter to 0.
- Iterate over the tickets array, reducing the ticket count for each person by one in each iteration (signifying the purchase of a ticket) and incrementing the time counter.
- After each person buys a ticket, check if the person at position k has finished buying their tickets. If so, break out of the loop.
- If a person's ticket count reaches zero, they leave the queue, but since we are iterating over the original array without modifying its structure, we treat it as if the person with zero tickets does not affect the loop anymore (their ticket count cannot go below zero).

> The time complexity is O(n*m) where n is the number of people in the queue and m is the maximum number of tickets a person wants to buy.

Here's how the code looks with these steps:

### Python
```python
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0  # Initialize the counter to keep track of the time
        while tickets[k] > 0:  # Loop until the person at position k has no tickets left to buy
            for i in range(len(tickets)):  # Iterate through each person in the line
                if tickets[i] > 0:  # If the person has tickets to buy
                    tickets[i] -= 1  # Buy a ticket
                    time += 1  # Increment the time
                if tickets[k] == 0:  # If the person at position k has bought all their tickets
                    return time  # Return the total time taken
        return time  # Just in case, but this line should never be reached as the function returns in the loop
```

### JavaScript
```javascript
/**
 * Calculates the time required for the k-th person to buy all their tickets.
 * @param {number[]} tickets - Array representing the number of tickets each person wants to buy.
 * @param {number} k - The index of the person in the queue.
 * @return {number} - The total time taken for the k-th person to buy all their tickets.
 */
var timeRequiredToBuy = function(tickets, k) {
    let time = 0; // Init time counter. Every tick is a ticket buy.
    while (tickets[k] > 0) { // Loop till k-th person's tickets are bought.
        for (let i = 0; i < tickets.length; i++) { // Simulate the queue movement.
            if (tickets[i] > 0) { // If person i has tickets to buy...
                tickets[i] -= 1; // ...they buy one.
                time += 1; // Increment the time for each ticket bought.
                if (tickets[k] === 0) return time; // If k-th person's done, exit early.
            }
        }
    }
    return time; // Safety net, but the logic ensures we exit in the loop.
};
```

### Java
```java
class Solution {
    /**
     * Simulates the process of buying tickets in a queue to determine the time it takes for the k-th person to buy all theirs.
     * @param tickets Array representing the number of tickets each person in the queue wants to buy.
     * @param k The index of the person whose total time to buy tickets we're calculating.
     * @return The total time taken for the person at index k to buy all their tickets.
     */
    public int timeRequiredToBuy(int[] tickets, int k) {
        int time = 0; // Init the stopwatch.
        while (tickets[k] > 0) { // Keep going till our k-th person is ticketless.
            for (int i = 0; i < tickets.length; i++) { // One loop = one sec, per person in line.
                if (tickets[i] > 0) { // If they've got tickets to buy...
                    tickets[i]--; // ...they buy one.
                    time++; // Crank the time up by one.
                    if (tickets[k] == 0) return time; // If k-th person's done, clock out early.
                }
            }
        }
        return time; // Just for formality. We exit via the loop.
    }
}
```

### C#
```csharp
public class Solution {
    /**
     * Simulates buying tickets in a queue to find out how long it takes for the k-th person to buy all of theirs.
     * @param tickets Array showing how many tickets each person wants to buy.
     * @param k Index of the person we're focusing on.
     * @return Total time taken for the k-th person to buy all their tickets.
     */
    public int TimeRequiredToBuy(int[] tickets, int k) {
        int time = 0; // Kicks off the timer.
        while (tickets[k] > 0) { // Loop 'til k's tickets are all bought.
            for (int i = 0; i < tickets.Length; i++) { // March through the queue.
                if (tickets[i] > 0) { // If someone still wants to buy...
                    tickets[i]--; // They get 1 ticket.
                    time++; // And the clock ticks once.
                    if (tickets[k] == 0) return time; // If k is done, we're done.
                }
            }
        }
        return time; // Technically unreachable, but here for completeness.
    }
}
```

> **Tags:** Queue, Simulation  
> **Difficulty:** Easy  
> **Migrated:** 2025-08-20 05:30:00 UTC
