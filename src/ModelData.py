class ModelData(object):

    def __init__(self, slots, parts):
        self.n_parts = len(parts)
        self.lengths = list(map(lambda part: part.length, parts))
        self.widths = list(map(lambda part: part.width, parts))
        self.weights = list(map(lambda part: 1, parts))

        self.n_slots = len(slots)
        self.slot_lengths = list(map(lambda slot: slot.length, slots))
        self.slot_widths = list(map(lambda slot: slot.width, slots))
        self.slot_capacity = list(map(lambda slot: slot.capacity, slots))

    def copy_data_to(self, instance):
        for key, value in instance.input.items():
            instance[key] = getattr(self, key)
        return instance
