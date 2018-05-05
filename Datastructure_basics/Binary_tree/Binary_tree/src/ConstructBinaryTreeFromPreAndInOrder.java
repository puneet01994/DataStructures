/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author puneet
 */
public class ConstructBinaryTreeFromPreAndInOrder {
        int preIndex = 0;
        Node buildTree(int in[], int pre[], int inStart, int inEnd){
        if(inStart> inEnd)
            return null;
        
        Node treeRoot = new Node(pre[preIndex++]);
        
        if(inStart == inEnd){
            return treeRoot;
        }
        
        int inIndex = getIndex(in, treeRoot.data, inStart, inEnd); 
        
        treeRoot.left = buildTree(in, pre, inStart, inIndex-1);
        treeRoot.right = buildTree(in, pre, inIndex+1, inEnd);
        
        return treeRoot;
        }
        
        int getIndex(int in[], int d, int start, int end){
//            int index = 0;
                int i;
            for(i = start; i<=end; i++){
                if(in[i] == d)
                    return i;
            }
            return i;
        }
}
