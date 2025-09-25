def compress(self, chars):
        write = 0  # position to write
        i = 0      # pointer to read

        while i < len(chars):
            char = chars[i]
            count = 0

            # Count occurrences of the same character
            while i < len(chars) and chars[i] == char:
                i += 1
                count += 1

            # Write character
            chars[write] = char
            write += 1

            # Write count if > 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write

        