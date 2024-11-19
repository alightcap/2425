private int size;

void Awake()
{

}

void Start()
{

}

void Update()
{

}

void OnCollisionEnter(Collision collision)
{
    if (collision.gameObject.CompareTag("Yobi"))
    {
        yobi = collision.gameObject.GetComponent<Yobi>();
        if (yobi.GetSize() < size)
        {
            size += yobi.GetSize();
            Destroy(collision.gameObject);
        }
        else
        {
            Debug.Log("Run Away!");
        }
    }
}
