class DataCollector(object):

    def __init__(self, print_collected_data=False):
        self.print_enabled = print_collected_data
        self.attribute_data = {'time': [], 'wasted_space_sum': [], 'grouped_parts': []}

    def collect(self, parts, result):
        for attribute in self.attribute_data:
            if hasattr(result.solution, attribute):
                self.attribute_data[attribute].append((len(parts), getattr(result.solution, attribute)))
                if self.print_enabled:
                    print(result.solution.wasted_space_sum)

        self.attribute_data["time"].append((len(parts), result.statistics['time'].total_seconds()))

    def get_data(self, attribute_name):
        return self.attribute_data[attribute_name]
