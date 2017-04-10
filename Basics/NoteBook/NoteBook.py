import datetime

last_id = 0


class Note:
    def __init__(self, memo, tags=''):
        self.memo = memo
        self.tags = tags
        self.createion_data = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        return filter in self.memo or filter in self.tags


class NoteBook:
    def __init__(self):
        self.notes = []

    def new_note(self, memo, tags=''):
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        note = self.find_note(note_id)
        if note:
            note.memo = memo
            return True
        return None

    def modify_tags(self, note_id, tags):
        for note in self.notes:
            if str(note.id) == str(note_id):
                note.tags = tags
                break

    def find_note(self, note_id):
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return False

    def search(self, filter):
        return [note for note in self.notes if note.match(filter)]

if __name__ == '__main__':
    book = NoteBook()
    book.new_note('eddie', 'python,java')
    book.new_note("java", "head first")
    book.new_note("python", "head first")
