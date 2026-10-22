import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Unit III - Project 9: 0/1 Knapsack Problem using Dynamic Programming
 * 
 * This program solves the classic 0/1 Knapsack optimization problem
 * using bottom-up tabular dynamic programming.
 * 
 * Dataset:
 *   Item 1: Weight = 1, Profit = 10
 *   Item 2: Weight = 2, Profit = 20
 *   Item 3: Weight = 4, Profit = 35
 *   Item 4: Weight = 5, Profit = 45
 *   Capacity: 10
 */
public class Project9_Knapsack_DP {

    // Data structure to represent an individual item
    static class Item {
        int id;
        int weight;
        int profit;

        Item(int id, int weight, int profit) {
            this.id = id;
            this.weight = weight;
            this.profit = profit;
        }
    }

    /**
     * Builds the DP table where dp[i][w] represents the maximum profit
     * obtainable using a subset of the first i items with knapsack capacity w.
     */
    public static int[][] buildDPTable(Item[] items, int capacity) {
        int n = items.length;
        int[][] dp = new int[n + 1][capacity + 1];

        for (int i = 1; i <= n; i++) {
            int currentWeight = items[i - 1].weight;
            int currentProfit = items[i - 1].profit;

            for (int w = 0; w <= capacity; w++) {
                if (currentWeight <= w) {
                    // Maximum of including or excluding the current item
                    dp[i][w] = Math.max(currentProfit + dp[i - 1][w - currentWeight], dp[i - 1][w]);
                } else {
                    // Cannot include current item; inherit solution from previous subset
                    dp[i][w] = dp[i - 1][w];
                }
            }
        }
        return dp;
    }

    /**
     * Backtracks through the DP table to determine the subset of items
     * included in the optimal solution.
     */
    public static List<Item> traceSelectedItems(int[][] dp, Item[] items, int capacity) {
        List<Item> selected = new ArrayList<>();
        int currentCapacity = capacity;
        int n = items.length;

        for (int i = n; i > 0; i--) {
            // If profit differs from cell directly above, item i was included
            if (dp[i][currentCapacity] != dp[i - 1][currentCapacity]) {
                selected.add(items[i - 1]);
                currentCapacity -= items[i - 1].weight;
            }
        }
        Collections.reverse(selected);
        return selected;
    }

    /**
     * Displays the complete Dynamic Programming matrix with formatted headers.
     */
    public static void printDPMatrix(int[][] dp, int n, int capacity) {
        System.out.println("\nDynamic Programming Table (Rows: Items 0 to " + n + " | Columns: Capacity 0 to " + capacity + "):");
        System.out.print("Cap -> ");
        for (int w = 0; w <= capacity; w++) {
            System.out.printf("%5d", w);
        }
        System.out.println();
        System.out.println("-------" + "-----".repeat(capacity + 1));

        for (int i = 0; i <= n; i++) {
            System.out.printf("Item %d|", i);
            for (int w = 0; w <= capacity; w++) {
                System.out.printf("%5d", dp[i][w]);
            }
            System.out.println();
        }
        System.out.println("-------" + "-----".repeat(capacity + 1));
    }

    public static void main(String[] args) {
        // Problem definition
        int knapsackCapacity = 10;
        Item[] items = {
            new Item(1, 1, 10),
            new Item(2, 2, 20),
            new Item(3, 4, 35),
            new Item(4, 5, 45)
        };

        System.out.println("=================================================================");
        System.out.println("        0/1 KNAPSACK PROBLEM - DYNAMIC PROGRAMMING APPROACH       ");
        System.out.println("=================================================================");
        System.out.println("Knapsack Maximum Capacity (W) : " + knapsackCapacity);
        System.out.println("Total Available Items (n)     : " + items.length);

        System.out.println("\nItem Set Details:");
        System.out.println("--------------------------------------------------");
        System.out.printf("%-10s %-15s %-15s\n", "Item ID", "Weight (kg)", "Profit ($)");
        System.out.println("--------------------------------------------------");
        for (Item item : items) {
            System.out.printf("Item %-5d %-15d %-15d\n", item.id, item.weight, item.profit);
        }
        System.out.println("--------------------------------------------------");

        // Solve using Dynamic Programming
        int[][] dpTable = buildDPTable(items, knapsackCapacity);

        // Display DP Matrix
        printDPMatrix(dpTable, items.length, knapsackCapacity);

        // Traceback selected items
        List<Item> chosenItems = traceSelectedItems(dpTable, items, knapsackCapacity);

        int maxProfit = dpTable[items.length][knapsackCapacity];
        int accumulatedWeight = 0;
        int accumulatedProfit = 0;

        System.out.println("\nOptimal Solution Summary:");
        System.out.println("--------------------------------------------------");
        System.out.println("Maximum Profit Achieved : " + maxProfit);
        System.out.println("Optimal Items Selected  :");
        for (Item item : chosenItems) {
            System.out.printf("  * Item %d (Weight: %d, Profit: %d)\n", item.id, item.weight, item.profit);
            accumulatedWeight += item.weight;
            accumulatedProfit += item.profit;
        }
        System.out.println("--------------------------------------------------");
        System.out.println("Total Knapsack Weight   : " + accumulatedWeight + " / " + knapsackCapacity + " capacity");
        System.out.println("Total Solution Profit   : " + accumulatedProfit);
        System.out.println("Capacity Constraint Met : " + (accumulatedWeight <= knapsackCapacity ? "YES (Valid)" : "NO (Exceeded)"));
        System.out.println("=================================================================");
    }
}
