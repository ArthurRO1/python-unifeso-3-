class Student:
    def __init__(self, nome, disciplina, matricula, senha):
        self.nome = nome
        self.disciplina = disciplina
        self.matricula = matricula
        self.senha = senha

    def __str__(self):
        return f"Nome: {self.nome}, Disciplina: {self.disciplina}, Matrícula: {self.matricula}"


class HashTable:
    def __init__(self, table_size=23, hash_function="divisao"):
        self.table_size = table_size
        self.table = [None] * table_size
        self.hash_function = hash_function
        self.collisions = 0

    # FUNÇÕES HASH 

    def hash_divisao(self, password):
        return len(password) % self.table_size

    def hash_multiplicacao(self, password):
        return int((len(password) * 0.618033988749) % self.table_size)

    def hash_ascii(self, password):
        return sum(ord(c) for c in password) % self.table_size

    def hash_djb2(self, password):
        hash_val = 5381
        for c in password:
            hash_val = ((hash_val << 5) + hash_val) + ord(c)
        return hash_val % self.table_size

    def get_hash(self, password):
        if self.hash_function == "divisao":
            return self.hash_divisao(password)

        elif self.hash_function == "multiplicacao":
            return self.hash_multiplicacao(password)

        elif self.hash_function == "ascii":
            return self.hash_ascii(password)

        elif self.hash_function == "djb2":
            return self.hash_djb2(password)

        else:
            raise ValueError("Função hash inválida")


    def insert(self, password, student_index):
        index = self.get_hash(password)

        original = index

        while self.table[index] is not None:
            self.collisions += 1
            index = (index + 1) % self.table_size

            if index == original:
                print("Tabela cheia!")
                return

        self.table[index] = (password, student_index)

    def search(self, password):
        index = self.get_hash(password)

        original = index

        while self.table[index] is not None:

            if self.table[index][0] == password:
                return self.table[index][1]

            index = (index + 1) % self.table_size

            if index == original:
                break

        return None

    def show_table(self):
        print("\nTabela Hash:")
        for i, item in enumerate(self.table):
            print(f"{i}: {item}")

        print(f"\nColisões: {self.collisions}")


class StudentManager:
    def __init__(self, hash_function="divisao"):
        self.students = []
        self.hash_table = HashTable(
            table_size=23,
            hash_function=hash_function
        )

    def add_student(self, nome, disciplina, matricula, senha):
        student = Student(
            nome,
            disciplina,
            matricula,
            senha
        )

        self.students.append(student)

        indice = len(self.students) - 1

        self.hash_table.insert(senha, indice)

    def buscar_por_senha(self, senha):
        indice = self.hash_table.search(senha)

        if indice is not None:
            return self.students[indice]

        return None

    def listar_alunos(self):
        for aluno in self.students:
            print(aluno)


# TESTE 

manager = StudentManager(hash_function="multiplicacao")

manager.add_student("Arthur", "EDP", "2025001", "senha123")
manager.add_student("Lucas", "EDP", "2025002", "abc123")
manager.add_student("Maria", "EDP", "2025003", "python")
manager.add_student("João", "EDP", "2025004", "estrutura")

print("\n=== LISTA DE ALUNOS ===")
manager.listar_alunos()

print("\n=== BUSCA POR SENHA ===")
resultado = manager.buscar_por_senha("python")

if resultado:
    print(resultado)
else:
    print("Aluno não encontrado")

manager.hash_table.show_table()