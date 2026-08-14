public class MyQueue
{
    Stack<int> stack1;
    Stack<int> temp;

    public MyQueue()
    {
        stack1 = new Stack<int>();
        temp = new Stack<int>();
    }

    public void Push(int x)
    {
        // Move everything from stack1 to temp
        int count1 = stack1.Count;

        for (int i = 0; i < count1; i++)
        {
            temp.Push(stack1.Pop());
        }

        // Put new value on top
        stack1.Push(x);

        // Move everything back to stack1
        int count2 = temp.Count;

        for (int i = 0; i < count2; i++)
        {
            stack1.Push(temp.Pop());
        }
    }

    public int Pop()
    {
        return stack1.Pop();
    }

    public int Peek()
    {
        return stack1.Peek();
    }

    public bool Empty()
    {
        return stack1.Count == 0;
    }
}