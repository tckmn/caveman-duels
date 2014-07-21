puts((ARGV.shift || "P,").match(/(.),/)[1] == "P" ? "S" : "P")
