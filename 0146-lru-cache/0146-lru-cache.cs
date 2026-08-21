public class LRUCache
{
    Dictionary<int, LinkedListNode<(int key, int value)>> hashmap
        = new Dictionary<int, LinkedListNode<(int key, int value)>>();

    LinkedList<(int key, int value)> list
        = new LinkedList<(int key, int value)>();

    int size;

    public LRUCache(int capacity)
    {
        size = capacity;
    }

    public int Get(int key)
    {
        if (!hashmap.ContainsKey(key))
            return -1;

        var node = hashmap[key];

        list.Remove(node);
        list.AddFirst(node);

        return node.Value.value;
    }

    public void Put(int key, int value)
    {
        if (hashmap.ContainsKey(key))
        {
            var node = hashmap[key];

            node.Value = (key, value);

            list.Remove(node);
            list.AddFirst(node);
        }
        else
        {
            if (list.Count >= size)
            {
                var removal = list.Last;

                hashmap.Remove(removal.Value.key);
                list.RemoveLast();
            }

            var node =
                new LinkedListNode<(int key, int value)>((key, value));

            list.AddFirst(node);
            hashmap[key] = node;
        }
    }
}