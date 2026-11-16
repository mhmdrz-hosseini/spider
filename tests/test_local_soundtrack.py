import json
import tempfile
import unittest
from pathlib import Path
from ketabyar_audio.local_soundtrack import eligible, index_library, beats_from, score, match

class SoundtrackTests(unittest.TestCase):
    def test_license(self):
        self.assertFalse(eligible({"license":"UNKNOWN"}))
        self.assertFalse(eligible({"license":"CC-BY-NC-4.0"}))
        self.assertTrue(eligible({"license":"CC0-1.0"}))
        self.assertFalse(eligible({"license":"CC-BY-4.0"}, True))
        self.assertTrue(eligible({"license":"CC-BY-4.0","creator":"A","source_url":"https://example.com","attribution":"A CC BY 4.0"}, True))

    def test_scene_adapter(self):
        scenes={"scenes":[{"scene_id":"s", "mood":"curious", "energy":2,
                            "states":[{"state_id":"a","start_sec":0,"end_sec":2},
                                      {"state_id":"b","start_sec":2,"end_sec":5}]}]}
        beats=beats_from(scenes)
        self.assertEqual(len(beats),1)
        self.assertEqual(beats[0]["end_sec"],5)

    def test_matching_prefers_mood_without_vocals(self):
        beat={"mood":"curious","energy":2,"start_sec":0,"end_sec":5,"keywords":[]}
        good={"id":"a","moods":["curious"],"energy":2,"tags":["piano"],"speech_friendly":True,"loopable":True}
        bad={"id":"b","moods":["tense"],"energy":5,"tags":["vocals"],"speech_friendly":False,"loopable":True}
        self.assertGreater(score(good,beat),score(bad,beat))

    def test_catalog_local_selection(self):
        with tempfile.TemporaryDirectory() as directory:
            folder=Path(directory)
            (folder/"curious_piano.wav").write_bytes(b"dummy")
            (folder/"unknown.mp3").write_bytes(b"dummy")
            (folder/"unknown.mp3.json").write_text('{"license":"UNKNOWN"}')
            catalog=index_library(folder,"CC0-1.0","https://example.com/verified")
            self.assertEqual(len(catalog["tracks"]),2)
            path=folder/"scenes.json"
            path.write_text(json.dumps({"beats":[{"id":"scene","start_sec":0,"end_sec":5,"mood":"curious","energy":2}]}))
            plan=match(folder/"catalog.json",path)
            self.assertEqual(plan["tracks"][0]["track_id"],"curious_piano.wav")

if __name__=="__main__":
    unittest.main()
