class ModelData(object):

    def __init__(self, slots, parts):
        self.n_parts = len(parts)
        self.lengths = []
        self.widths = []
        self.weights = []

        for part in parts:
            self.lengths.append(part.length)
            self.widths.append(part.width)
            self.weights.append(1)

        self.n_slots = len(slots)
        self.slot_lengths = []
        self.slot_widths = []
        self.slot_capacity = []

        for slot in slots:
            self.slot_lengths.append(slot.length)
            self.slot_widths.append(slot.width)
            self.slot_capacity.append(slot.capacity)

    def copy_data_to(self, instance):
        for key, value in instance.input.items():
            instance[key] = getattr(self, key)
        return instance
