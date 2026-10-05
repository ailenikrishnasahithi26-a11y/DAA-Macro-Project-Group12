import java.util.ArrayList;
import java.util.List;

/**
 * Sum of Subsets Problem Using Backtracking
 * Given Set: S = {5, 10, 12}
 * Target Sum: M = 15
 */
public class SumOfSubsets {

    public static void findSubsets(int index, List<Integer> currentSubset, int currentSum,
                                   int targetSum, int[] elements) {

        // Base Case 1: Target reached
        if (currentSum == targetSum) {
            System.out.println("Valid Subset Found: " 
                + currentSubset.toString().replace('[', '{').replace(']', '}') 
                + " (Sum = " + currentSum + ")");
            return;
        }

        // Base Case 2: Pruning Condition (Bounding Function)
        if (currentSum > targetSum) {
            return; // Prune branch immediately
        }

        // Base Case 3: Reached end of elements without match
        if (index >= elements.length) {
            return;
        }

        // Choice 1: Include elements[index]
        currentSubset.add(elements[index]);
        findSubsets(index + 1, currentSubset, currentSum + elements[index], targetSum, elements);

        // Backtracking Step: Undo Choice 1
        currentSubset.remove(currentSubset.size() - 1);

        // Choice 2: Exclude elements[index]
        findSubsets(index + 1, currentSubset, currentSum, targetSum, elements);
    }

    public static void main(String[] args) {
        int[] S = {5, 10, 12};
        int M = 15;

        System.out.println("=============================================");
        System.out.println("    SUM OF SUBSETS USING BACKTRACKING");
        System.out.println("=============================================");
        System.out.print("Input Set   : {");
        for (int i = 0; i < S.length; i++) {
            System.out.print(S[i] + (i < S.length - 1 ? ", " : ""));
        }
        System.out.println("}");
        System.out.println("Target Sum  : " + M);
        System.out.println("---------------------------------------------");

        findSubsets(0, new ArrayList<>(), 0, M, S);

        System.out.println("=============================================");
    }
}
