def show_tasks(tasks):
    print("\n📝 Tumhari To-Do List:")
    print("=" * 30)
    if len(tasks) == 0:
        print("Koi task nahi hai!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print("=" * 30)

def todo_app():
    tasks = []
    print("=" * 30)
    print("   📝 To-Do List App!")
    print("=" * 30)

    while True:
        print("\nKya karna hai?")
        print("1. Task add karo")
        print("2. Task delete karo")
        print("3. Tasks dekho")
        print("4. Exit")

        choice = input("\nOption choose karo (1/2/3/4): ")

        if choice == "1":
            task = input("Naya task likho: ")
            tasks.append(task)
            print(f"✅ '{task}' add ho gayi!")

        elif choice == "2":
            show_tasks(tasks)
            if len(tasks) > 0:
                num = int(input("Konsi task delete karni hai? (number): "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"🗑️ '{removed}' delete ho gayi!")
                else:
                    print("❌ Galat number!")

        elif choice == "3":
            show_tasks(tasks)

        elif choice == "4":
            print("Bye! 👋")
            break

        else:
            print("❌ Galat option! 1, 2, 3 ya 4 choose karo!")

todo_app()