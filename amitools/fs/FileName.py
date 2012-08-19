from FSString import FSString

class FileName:
  root_path_aliases = (u'', u'/', u':')
  
  def __init__(self, name, is_intl=False):
    # check that name is a FSString
    if not isinstance(name, FSString):
      raise ValueError("FileName's name must be a FSString")
    self.name = name
    self.is_intl = is_intl
  
  def __str__(self):
    return self.name
  
  def __repr__(self):
    return self.name
  
  def is_root_path_alias(self):
    return self.name.get_unicode() in self.root_path_aliases
  
  def split_path(self):
    pc = self.name.get_unicode().split("/")
    p = []
    for path in pc:
      p.append(FileName(FSString(path), is_intl=self.is_intl))
    return p
  
  def get_dir_and_base_name(self):
    """Return portion after last slash '/' or the full name in unicode"""
    s = self.name.get_unicode()
    pos = s.rfind(u'/')
    if pos != -1:
      dir_name = s[:pos]
      file_name = s[pos+1:]
      if len(file_name) == 0:
        return FSString(dir_name), None
      else:
        return FSString(dir_name), FSString(file_name)
    else:
      return None, self.name
    
  def get_upper_ami_str(self):
    result = self.name.get_ami_str().upper();
    if self.is_intl:
      r = ""
      for i in xrange(len(result)):
        o = ord(result[i])
        if o >= 224 and o <= 254 and o != 247:
          r += chr(o - (ord('a')-ord('A')))
        else:
          r += chr(o)
      return r
    else:
      return result
  
  def is_valid(self):
    s = self.name.get_ami_str()
    if len(s) > 30:
      return False
    for c in s:
      o = ord(c)
      if o == ':' or o == '/':
        return False
      if not self.is_intl and o > 127:
        return False
    return True
  
  def hash(self, hash_size=72):
    up = self.get_upper_ami_str();
    h = len(up)
    for c in up:
      h = h * 13;
      h += ord(c)
      h &= 0x7ff
    h = h % hash_size
    return h

  def get_name(self):
    """Return file name string as a FSString."""
    return self.name

  def get_ami_str_name(self):
    return self.name.get_ami_str()
  
  def get_unicode_name(self):
    return self.name.get_unicode()
