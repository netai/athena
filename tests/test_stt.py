#!/usr/bin/env python2
# -*- coding: utf-8-*-
import unittest
import imp
from client import stt, athenapath


def cmuclmtk_installed():
    try:
        imp.find_module('cmuclmtk')
    except ImportError:
        return False
    else:
        return True


def pocketsphinx_installed():
    try:
        imp.find_module('pocketsphinx')
    except ImportError:
        return False
    else:
        return True


@unittest.skipUnless(cmuclmtk_installed(), "CMUCLMTK not present")
@unittest.skipUnless(pocketsphinx_installed(), "Pocketsphinx not present")
class TestSTT(unittest.TestCase):

    def setUp(self):
        self.athena_clip = athenapath.data('audio', 'athena.wav')
        self.time_clip = athenapath.data('audio', 'time.wav')

        self.passive_stt_engine = stt.PocketSphinxSTT.get_passive_instance()
        self.active_stt_engine = stt.PocketSphinxSTT.get_active_instance()

    def testTranscribeathena(self):
        """
        Does athena recognize his name (i.e., passive listen)?
        """
        with open(self.athena_clip, mode="rb") as f:
            transcription = self.passive_stt_engine.transcribe(f)
        self.assertIn("athena", transcription)

    def testTranscribe(self):
        """
        Does athena recognize 'time' (i.e., active listen)?
        """
        with open(self.time_clip, mode="rb") as f:
            transcription = self.active_stt_engine.transcribe(f)
        self.assertIn("TIME", transcription)
