# techpaf-s2e05-katas

Des starters pour commencer rapidement les katas pour différents langages.

## Fizz Buzz

* [Le kata Fizz Buzz sur kata-log.rocks](http://kata-log.rocks/fizz-buzz-kata)


### Ta tâche

* écris un programme qui affiche une ligne pour chaque nombre de 1 à 100
* pour les multiples de 3 écris `Fizz` à la place du nombre
* pour les multiples de 5 écris `Buzz` à la place du nombre
* pour les nombres qui sont des multiples de 3 et 5 écris `FizzBuzz` à la place du nombre

### Points de départ

Des points de départ pour plusieurs langages sont présents dans ce repo.

* [Java maven Junit5](fizzbuzz/kata-fizzbuzz-java)
* [Kotlin maven kotlin-test](fizzbuzz/kata-fizzbuzz-kotlin)
* [Javascript (es6) nodejs jest](fizzbuzz/kata-fizzbuzz-js-jest)
* [Javascript vanilla qunit](fizzbuzz/kata-fizzbuzz-js-vanilla-qunit) ne requiert pas npm et peut être lancé dans un navigateur
* [Elixir](fizzbuzz/kata-fizzbuzz-elixir)
* [Python pytest](fizzbuzz/kata-fizzbuzz-python/pytest)
* [Python unittest](fizzbuzz/kata-fizzbuzz-python/unittest)

## Contraintes

Si le sujet te semble très (trop?) facile tu peux y ajouter des contraintes.

Voici des exemples de contraintes.

* Pas de `if`, `switch` ou de boucle
* Dans un langage que tu ne connais pas
* [Mob programming](http://kata-log.rocks/mob-programming)
* [Mute ping-pong](http://kata-log.rocks/mute-ping-pong)
* [Object calisthenics](https://williamdurand.fr/2013/06/03/object-calisthenics/)
* [tell don't ask!](http://kata-log.rocks/tell-dont-ask)
* [no primitives](http://kata-log.rocks/no-primitives)
* [simple design](http://kata-log.rocks/simple-design)
* [the 70s compiler](http://kata-log.rocks/the-70s-compiler)

### Baby steps

  1. mettre en place un repo git (ou autre mais qui doit supporter `reset`)
  2. Mettre un timer de 2 minutes quand on commence
  3. écrire exactement 1 test
      * si le timer sonne et que le test est rouge `revert` et tout recommencer
      * si le test est vert avant la fin du timer, réinitialise le timer et continue
  4. redémarre le timer
  5. retour à l'étape iii.
  
#### Astuces

* chaque paire devrait 'reset' au moins une fois
* c'est tout à fait normal de passer des itérations pour faire uniquement des refactorings (tant que les tests sont vert c'est OK)
* ne pas hesiter à discuter sur ce qui peut être nécessaire entre les cycles
* la partie la plus importante est d'avoir des tests verts. Ta code base ne devrait jamais être au rouge moins de 2 minutes


