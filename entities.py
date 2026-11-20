class User:
    def __init__(self, user_id, username, balance, favorites, subscription):
        self.user_id = user_id
        self.username = username
        self.balance = balance
        self.favorites = favorites
        self.subscription = subscription


class Game:
    def __init__(self, game_id, title, description, cover, genres, price, is_free, activation_data, store="steam"):
        self.game_id = game_id
        self.title = title
        self.description = description
        self.cover = cover
        self.genres = genres
        self.price = price
        self.is_free = is_free
        self.activation_data = activation_data
        self.store = store


class OrderAndRefund:
    def __init__(self, receipt_id, user_id, game_id, amount, purchase_time, refund_requested, refund_approved, refund_time):
        self.receipt_id = receipt_id
        self.user_id = user_id
        self.game_id = game_id
        self.amount = amount
        self.purchase_time = purchase_time
        self.refund_requested = refund_requested
        self.refund_approved = refund_approved
        self.refund_time = refund_time


class Library:
    def __init__(self, user_id, games, activation_map, sort_by):
        self.user_id = user_id
        self.games = games
        self.activation_map = activation_map
        self.sort_by = sort_by


class Subscription:
    def __init__(self, sub_id, user_id, plan, price, start_time, end_time, auto_renew, active, early_access, fee_discount):
        self.sub_id = sub_id
        self.user_id = user_id
        self.plan = plan
        self.price = price
        self.start_time = start_time
        self.end_time = end_time
        self.auto_renew = auto_renew
        self.active = active
        self.early_access = early_access
        self.fee_discount = fee_discount


class CatalogAndBanners:
    def __init__(self, games, free_now, max_value, banners, store="steam"):
        self.games = games
        self.free_now = free_now
        self.max_value = max_value
        self.banners = banners
        self.store = store
 
#---------------------------#       
        
class User:
    def __init__(self, uid, name, balance, favs, sub):
        self.uid, self.name, self.balance, self.favs, self.sub = uid, name, balance, favs, sub
        self.cart = []

    def pick_game(self, game):
        if game not in self.cart:
            self.cart.append(game)

    def pay(self, amount, base_fee=0):
        fee = self.sub.calc_fee(base_fee) if self.sub else base_fee
        if self.balance >= amount + fee:
            self.balance -= amount + fee
            return True
        return False


class Game:
    def __init__(self, gid, title, desc, cover, genres, price, free, key, store="steam"):
        self.gid, self.title, self.desc, self.cover = gid, title, desc, cover
        self.genres, self.price, self.free, self.key, self.store = genres, price, free, key, store


class Library:
    def __init__(self, uid, games, keys, sort_by):
        self.uid, self.games, self.keys, self.sort_by = uid, games, keys, sort_by

    def add_game(self, game):
        if game not in self.games:
            self.games.append(game)
            self.keys[game.gid] = game.key

    def remove_game(self, gid):
        self.games = [g for g in self.games if g.gid != gid]
        self.keys.pop(gid, None)


class Subscription:
    def __init__(self, sid, uid, plan, price, start, end, renew, active, early, disc):
        self.sid, self.uid, self.plan, self.price = sid, uid, plan, price
        self.start, self.end, self.renew, self.active, self.early, self.disc = start, end, renew, active, early, disc

    def calc_fee(self, base_fee):
        return max(0, base_fee * (1 - self.disc)) if self.active else base_fee


class Catalog:
    def __init__(self, games, free_now, max_val, banners, store="steam"):
        self.games, self.free_now, self.max_val, self.banners, self.store = games, free_now, max_val, banners, store

    def add_game(self, game):
        if game not in self.games:
            self.games.append(game)

    def search(self, q):
        return [g for g in self.games if g.store == self.store and q.lower() in g.title.lower()]

    def filter_games(self, genre=None, max_price=None, only_free=False):
        return [
            g for g in self.games
            if g.store == self.store
            and (not only_free or g.free)
            and (not genre or genre in g.genres)
            and (max_price is None or g.price <= max_price)
        ]