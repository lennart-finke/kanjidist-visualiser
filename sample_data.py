import random
import string
import json

def generate_kanji(n):
  """
  Generates n random kanji characters.

  Args:
      n: The number of kanji characters to generate.

  Returns:
      A list of n random kanji characters.
  """
  kanji_list = list(string.printable)
  kanji_list = set("どこで生れたかとんと見当がつかぬ。何でも薄暗いじめじめした所でニャーニャー泣いていた事だけは記憶している。吾輩はここで始めて人間というものを見た。しかもあとで聞くとそれは書生という人間中で一番獰悪な種族であったそうだ。この書生というのは時々我々を捕えて煮て食うという話である。しかしその当時は何という考もなかったから別段恐しいとも思わなかった。ただ彼の掌に載せられてスーと持ち上げられた時何だかフワフワした感じがあったばかりである。掌の上で少し落ちついて書生の顔を見たのがいわゆる人間というものの見始であろう。この時妙なものだと思った感じが今でも残っている。第一毛をもって装飾されべきはずの顔がつるつるしてまるで薬缶だ。その後猫にもだいぶ逢ったがこんな片輪には一度も出会わした事がない。のみならず顔の真中があまりに突起している。そうしてその穴の中から時々ぷうぷうと煙を吹く。どうも咽せぽくて実に弱った。これが人間の飲む煙草というものである事はようやくこの頃知った。この書生の掌の裏でしばらくはよい心持に坐っておったが、しばらくすると非常な速力で運転し始めた。書生が動くのか自分だけが動くのか分らないが無暗に眼が廻る。胸が悪くなる。到底助からないと思っていると、どさりと音がして眼から火が出た。それまでは記憶しているがあとは何の事やらいくら考え出そうとしても分らない。ふと気が付いて見ると書生はいない。たくさんおった兄弟が一疋も見えぬ。肝心の母親さえ姿を隠してしまった。その上今までの所とは違って無暗に明るい。眼を明いていられぬくらいだ。はてな何でも容子がおかしいと、のそのそ這い出して見ると非常に痛い。吾輩は藁の上から急に笹原の中へ棄てられたのである。我儘もこのくらいなら我慢するが吾輩は人間の不徳についてこれよりも数倍悲しむべき報道を耳にした事がある")
  return random.sample(sorted(kanji_list), n)

def generate_distances(n):
  """
  Generates a random upper triangular distance matrix.

  Args:
      n: The size of the matrix.

  Returns:
      A list of lists representing the upper triangular distance matrix.
  """
  distances = [[] for i in range(1, n)]
  for i in range(n):
    for j in range(i + 1, n):
      distances[i].append(random.random())
  return distances

def generate_data(n):
  """
  Generates a dictionary containing character names and distances.

  Args:
      n: The number of characters.

  Returns:
      A dictionary containing "characters" and "distances" keys.
  """
  characters = generate_kanji(n)
  distances = generate_distances(n)
  return {"characters": characters, "distances": distances}

# We create sample data of random distances between 
data = generate_data(50)
print(data)

# Save data to a JSON file
with open("data.json", "w") as f:
  json.dump(data, f)