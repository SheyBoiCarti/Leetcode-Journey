public class MyStack {

    private Queue<int> q;

    public MyStack() {
        q = new Queue<int>();
    }
    
    public void Push(int x) {
        q.Enqueue(x);

        //  Rotate previous elements so the new element reaches the front
        int size = q.Count;
        for (int i = 0; i < size - 1; i++) {
            q.Enqueue(q.Dequeue());
        }
    }
    
    public int Pop() {
        return q.Dequeue();
    }
    
    public int Top() {
        return q.Peek();
    }
    
    public bool Empty() {
        return q.Count == 0;
    }
}