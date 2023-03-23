class sequence_las:

    def __init__(self, start_sequence):
        self.start_sequence = start_sequence

    def raw_of_las_sequence(self, number_of_last_element):
        """Return a list of las-sequence up to number_of_last_element element"""
        final_raw = [self.start_sequence]
        counter=0
        last_symbol_read =  None

        for i in range(number_of_last_element-1): # i - номер предыдущего числа в ряде
            final_raw.append('')
            for j in str(final_raw[i]):
                if last_symbol_read == None:
                    last_symbol_read = j
                    counter += 1
                else:
                    if j == last_symbol_read:
                        counter += 1
                    else:
                        final_raw[i+1] += str(counter)+str(last_symbol_read)
                        counter = 1
                        last_symbol_read = j

            if counter != 0 :
                final_raw[i + 1] += str(counter) + str(last_symbol_read)
                counter = 0
            last_symbol_read = None;

        return final_raw
