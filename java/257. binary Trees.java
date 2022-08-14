/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private List<String> ans = new ArrayList<>();
    public List<String> binaryTreePaths(TreeNode root) {
        travelInOrder(root, "");
        return ans;
    }
    
    public void travelInOrder(TreeNode current, String totalValue){
        String value = String.valueOf(current.val);
        totalValue += value;
        
        if(current.left != null || current.right != null){
            totalValue += "->";
        }
        if(current.left != null){
            travelInOrder(current.left, totalValue);
        }
        if(current.right != null){
            travelInOrder(current.right, totalValue);
        }
        if(current.left == null && current.right == null){
            ans.add(totalValue);
        }
    }
}