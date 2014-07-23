me, he = (ARGV[0] || ' , ').split(',')

@possible_actions = %w[Sharpen Poke Block]

class String

  def sharpness
    @sharpness ||= count('S') - count('P')
  end

  def has_pointy_stick
    (1..4).cover? sharpness
  end

  def has_sword
    sharpness >= 5
  end

  def scary
    sharpness > 0
  end

end

def no action
  @possible_actions.delete(action)
end

def do!
  puts @possible_actions.sample[0]
end

no 'Block' if not he.has_pointy_stick

no 'Poke' if not me.scary

no 'Sharpen' if me.has_sword

no 'Block' if me.has_sword

do!