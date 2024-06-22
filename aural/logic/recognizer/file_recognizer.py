from time import time
from typing import Dict

import aural.logic.decoder as decoder
from aural.base_classes.base_recognizer import BaseRecognizer
from aural.config.settings import (ALIGN_TIME, FINGERPRINT_TIME, QUERY_TIME,
                                    RESULTS, TOTAL_TIME)


class FileRecognizer(BaseRecognizer):
    def __init__(self, aural):
        super().__init__(aural)

    def recognize_file(self, filename: str) -> Dict[str, any]:
        channels, self.Fs, _ = decoder.read(filename, self.aural.limit)

        t = time()
        matches, fingerprint_time, query_time, align_time = self._recognize(*channels)
        t = time() - t

        results = {
            TOTAL_TIME: t,
            FINGERPRINT_TIME: fingerprint_time,
            QUERY_TIME: query_time,
            ALIGN_TIME: align_time,
            RESULTS: matches
        }
        # print("here i return!")
        # print(results)
        # print("\n")
        return results
        # if results[RESULTS]:
        #     first_song_name = results[RESULTS][0]['song_name'].decode('utf-8')
        #     return first_song_name
        # else:
        #     return "No match found"

    def recognize(self, filename: str) -> Dict[str, any]:
        return self.recognize_file(filename)
