import { User, Token } from '@/types';

export interface IAuthState {
    user: User;
    token: Token;
}

export const AuthDefaultState = (): IAuthState => {
    return {
        user: { id: 0, email: '', created_at: 0 },
        token: { sub: '', exp: '', scopes: [] },
    };
};
