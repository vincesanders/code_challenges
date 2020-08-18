/**
 * // Definition for a Node.
 * function Node(val,prev,next,child) {
 *    this.val = val;
 *    this.prev = prev;
 *    this.next = next;
 *    this.child = child;
 * };
 */

/**
 * @param {Node} head
 * @return {Node}
 */
const flatten = function(head) {
    if (head === null) {
        return head;
    }

    //Make a new head, so prev is never null.
    const newHead = new Node(null, null, head, null);
    flattenDFS(newHead, head);

    newHead.next.prev = null;
    return newHead.next;
}

const flattenDFS = function(prev, current) {
    if (current === null) {
        return prev;
    }

    current.prev = prev;
    prev.next = current;

    const oldNext = current.next;
    const tail = flattenDFS(current, current.child);
    current.child = null;
    return flattenDFS(tail, oldNext);
}