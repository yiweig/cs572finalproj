from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals


from sumy._compat import to_unicode
from sumy.utils import cached_property
from sumy.models.dom import Sentence, Paragraph, ObjectDocumentModel
from sumy.parsers.parser import DocumentParser



#The built in plaintext parser takes in a format where there are headings (all uppercase) to denoted separation of paragraphs in text
#Need to write this class if you want to use modify sumy


class RawTextParser(DocumentParser):

        
    @classmethod
    def from_string(cls, string, tokenizer):
        return cls(string, tokenizer)
        
        
    @classmethod
    def from_file(cls, file_path, tokenizer):
        with open(file_path) as file:
            return cls(file.read(), tokenizer)
            
    def __init__(self, text, tokenizer):
        super(RawTextParser, self).__init__(tokenizer)
        self._text = to_unicode(text).strip()