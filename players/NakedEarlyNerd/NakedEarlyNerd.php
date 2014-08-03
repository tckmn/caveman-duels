<?php
    // me see how sharp the sticks
    class History {
        public function __construct ($str)
        {
            $this->sharpness = 0;
            for ($i = 0 ; $i != strlen ($str) ; $i++)
            {
                switch ($str{$i})
                {
                    case 'S' : $this->sharpness++; break;
                    case 'P' : if ($this->sharpness > 0) $this->sharpness--; break;
                }
            }
        }
    }

    // me get headache
    function think ($own, $foe)
    {
        // me no want no blunt stick
        if ($own->sharpness == 0)                   return "S";

        // maybe he blocks me, maybe he blocks me not
        if ($foe->sharpness == 0)                   return "SP";

        // good stick, me rather poke
        if ($own->sharpness - $foe->sharpness > 1)  return "SPPP";

        // not so good stick, me rather sharpen
                                                    return "SSSP";
    }

    // me go and fight
    $hist = count ($argv) == 2 ? $argv[1] : ',';
    list ($own, $foe) = explode (',', $hist);
    $answer = str_shuffle(think(new History ($own), new History ($foe)));
    echo $answer{0};
    ?>