/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author puneet
 */
import java.io.PrintStream;
import java.util.LinkedList;

public class Binary_tree
{
  Node root;
  
  public Binary_tree() {}
  
  LinkedList<Node> queue1 = new LinkedList();
  
//  Insert a node in the tree(BFS)
  public void insert_Node(int d) {
    Node n = new Node(d);
    if (root == null) {
      root = n;
    }
    else {
      Node front = queue1.getFirst();
      if (front.left == null) {
        front.left = n;
      }
      else if (front.right == null) {
        front.right = n;
      }
      if ((front.left != null) && (front.right != null)) {
        queue1.remove();
      }
    }
    queue1.add(n);
  }
  
//  Level Order Traversal of a bunary tree.
  public void levelOrderTraversal()
  {
    LinkedList<Node> traverse = new LinkedList();
    traverse.add(root);
    System.out.println("Level Order Traversal...");
    while (!traverse.isEmpty()) {
      Node node = traverse.poll();
      System.out.print(node.data + ", ");
      if (node.left != null) {
        traverse.add(node.left);
      }
      if (node.right != null) {
        traverse.add(node.right);
      }
    }
  }
  
//  In order traversal of a binary tree.
  public void inOrderTraversal(Node node)
  {
    if (node == null) {
      return;
    }
    inOrderTraversal(node.left);
    System.out.print(node.data + ", ");
    inOrderTraversal(node.right);
  }
  
//  Pre Order traversal of a binary tree.
  public void preOrderTraversal(Node node) {
    if (node == null) {
      return;
    }
    System.out.print(node.data + ", ");
    preOrderTraversal(node.left);
    preOrderTraversal(node.right);
  }
  
//  Post order traversal
  public void postOrderTraversal(Node node) {
    if (node == null) {
      return;
    }
    postOrderTraversal(node.left);
    postOrderTraversal(node.right);
    System.out.print(node.data + ", ");
  }
// Lowest Common ancestor of two nodes in a binary tree.
//  Print statements are just to understand recursion.
  public Node FindLCA(Node node, int n1, int n2){
    if(node == null){
        System.out.println("Node is null");
        return null;
    }
    if(node.data == n1 || node.data == n2){
        System.out.println("Function Call with "+node.data);
        return node;
    }
    
    System.out.println("Function Call With $$$$$$$$$"+node.data);
    
    Node left_lca = FindLCA(node.left, n1, n2);
    if (left_lca != null)
    System.out.println("###"+left_lca.data);
    else
        System.out.println("left_lca null");
    Node right_lca = FindLCA(node.right, n1, n2);
    if (right_lca != null)
    System.out.println("***"+right_lca.data);
    else
        System.out.println("right_lca null");
    
    
    if(left_lca != null && right_lca != null){
        System.out.println("IF......");
        return node;
    }
    
    if (left_lca != null){
        System.out.println("HERE RIGHT LCA IS NULL ");
        return left_lca;
    }
        
    else {
        System.out.println("HERE LEFT LCA IS NULL ");
        return right_lca;
    }
    }
}