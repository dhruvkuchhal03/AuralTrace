import abc
from time import time
from typing import Dict, List, Tuple

import numpy as np

from aural.config.settings import DEFAULT_FS


class BaseRecognizer(object, metaclass=abc.ABCMeta):
    def __init__(self, aural):
        self.aural = aural
        self.Fs = DEFAULT_FS

    def _recognize(self, *data) -> Tuple[List[Dict[str, any]], int, int, int]:
        # print("Starting _recognize...")
        fingerprint_times = []
        hashes = set()  # to remove possible duplicated fingerprints we built a set.
        for channel in data:
            # print(f"Processing channel {channel}")
            fingerprints, fingerprint_time = self.aural.generate_fingerprints(channel, Fs=self.Fs)
            fingerprint_times.append(fingerprint_time)
            hashes |= set(fingerprints)

        # print(f"Generated {len(hashes)} unique hashes")
        matches, dedup_hashes, query_time = self.aural.find_matches(hashes)

        # print(f"Fingerprinting time: {np.sum(fingerprint_times)}")
        # print(f"Query time: {query_time}")

        t = time()
        final_results = self.aural.align_matches(matches, dedup_hashes, len(hashes))
        align_time = time() - t

        # print(f"Align time: {align_time}")
        # print(f"Final results: {final_results}")
        # print("Exiting _recognize...")

        return final_results, np.sum(fingerprint_times), query_time, align_time

    @abc.abstractmethod
    def recognize(self) -> Dict[str, any]:
        pass  # base class does nothing
