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
    private List<String> answer = new ArrayList<String>();
    public List<String> binaryTreePaths(TreeNode root) {
        visit(root, "");
        return this.answer;
    }

    public void visit(TreeNode node, String route){
        if(node != null){
            route += node.val;
            if(node.left !=null || node.right != null){
                route += "->";
            }
            if(node.left != null){
                visit(node.left, route);
            }
            if(node.right != null){
                visit(node.right, route);
            }
            if(node.right == null && node.left == null){
                this.answer.add(route);
            }
        }
    }
}